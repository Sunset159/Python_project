import json
import os
from typing import Any
from pathlib import Path

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

BASE_DIR = Path(__file__).parent 
FILENAME = BASE_DIR / "tasks.json"

def check_number(number: int):
    if number:
        input("\nОшибка: номер не может быть пустым.\nНажмите любую кнопку для продолжения...")
        return False
    elif not number.isdigit():
        input("\nОшибка: номер должен быть числом\nНажмите любую кнопку для продолжения...")
        return False
    else:
        return True

class Task:
    def  __init__(self, description: str, status: bool = False, category: str | None = None):
        self.description = description
        self.status = status
        self.category = category

    def _status_done(self):
        self.status = True
    
    def _status_undone(self):
        self.status = False
    
    def __repr__(self):
        return (f"Task[description={self.description}, status={self.status}, category={self.category}]")
    
    def __str__(self):
        done = "[X]" if self.status else "[ ]"
        cat = f"{self.category}" if self.category else ""
        return f"- {done} {self.description} {cat}"
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "description": self.description,
            "status": self.status,
            "category": self.category
        }
    
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        return cls(
            description=data["description"],
            status=data.get("status", False),
            category=data["category"]
        )
    
class TaskTracker:
    def __init__(self):
        self._tasks: list[Task] = []

    def _add_task(self, description: str, status: bool = False, category: str | None = None) -> Task:
        task = Task(description, status=False, category=category)
        self._tasks.append(task)
        return task
    
    def _remove_task(self, index: int) -> None:
        if 0 <= index < len(self._tasks):
            del self._tasks[index]
        else:
            raise IndexError("Нет задачи с таким индексом")
        
    def _get_task(self, index: int) -> Task:
        if 0 <= index < len(self._tasks):
            return self._tasks[index]
        raise IndexError("Нет задачи с таким индексом")
    
    def _task_done(self, index: int) -> None:
        if 0 <= index < len(self._tasks):
            self._get_task(index)._status_done()
        else:
            raise IndexError("Нет задачи с таким индексом")
    
    def _task_undone(self, index: int) -> None:
        self._get_task(index)._status_undone()
        if 0 <= index < len(self._tasks):
            self._get_task(index)._status_undone()
        else:
            raise IndexError("Нет задачи с таким индексом")
    
    def _list_tasks(self, only_done: bool | None = None, category: str | None = None) -> list[Task]:
        result = self._tasks

        if only_done is True:
            result = [temp for temp in result if temp.status]
        elif only_done is False:
            result = [temp for temp in result if not temp.status]

        if category is not None:
            result = [temp for temp in result if temp.category == category]
        return result

    def __len__(self):
        return len(self._tasks)

    def __iter__(self):
        return iter(self._tasks) 
        
    def __repr__(self):
        return f"TaskTracker({self._tasks!r})"
    
    def _save_to_file(self, path: str) -> None:
        data = [task.to_dict() for task in self._tasks]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _load_from_file(self,path: str) -> None:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            self._tasks = []
            return
        
        self._tasks = [Task.from_dict(item) for item in data]

if __name__ == '__main__':
    tracker = TaskTracker()
    tracker._load_from_file(FILENAME)
    while True:
        clear()
        print("Меню:\n" \
                "1 - Показать все задачи\n" \
                "2 - Добавить задачу и категорию\n" \
                "3 - Удалить задачу\n" \
                "4 - Выполнить задачу\n" \
                "5 - Убрать отметку о выполнении у задачи\n" \
                "6 - Вывести все выполненные задачи\n" \
                "7 - Вывести все невыполненные задачи\n" \
                "8 - Вывести все задачи с заданной категорией\n" \
                "0 - Выход"
            )
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            print("\nЗадачи:")
            for i, task in enumerate(tracker, start=1):
                print(i, task)
            input("\nНажмите любую кнопку для продолжения...")
        elif choice == "2":
            description = input("Введите описание задачи: ").strip()
            cat = input("Введите категорию: ").strip().lower()
            
            if cat[0] != "#":
                cat = '#' + cat

            tracker._add_task(description, category=cat)

            print("Задача добавлена.")
            input("\nНажмите любую кнопку для продолжения...")          
        elif choice == "3":
            for i, task in enumerate(tracker, start=1):
                print(i, task)
    
            ind_del = int(input("Введите номер задачи, которую хотите удалить: ")) - 1
            tracker._remove_task(ind_del)

            print("Задача удалена.")
            input("\nНажмите любую кнопку для продолжения...")
        elif choice == "4":
            print("\nЗадачи:")
            for i, task in enumerate(tracker, start=1):
                print(i, task)
            
            done_task_by_index = int(input("\nВведите номер задачи, которую выполнили: ")) - 1

            tracker._task_done(done_task_by_index)
            print("Задача выполнена.")
            input("\nНажмите любую кнопку для продолжения...")
        elif choice == "5":
            print("\nЗадачи:")
            for i, task in enumerate(tracker, start=1):
                print(i, task)
            
            undone_task_by_index = int(input("\nВведите номер задачи, где хотите убрать статус о выполнении: ")) - 1

            tracker._task_undone(undone_task_by_index)
            print("Статус изменен.")
            input("\nНажмите любую кнопку для продолжения...")
        elif choice == "6":
            done_tasks = tracker._list_tasks(only_done=True)

            if not done_tasks:
                print("Нет выполненных задач.")
            else:
                for i, task in enumerate(done_tasks, start=1):
                    print(i, task)

            input("\nНажмите любую кнопку для продолжения...")
        elif choice == "7":
            undone_tasks = tracker._list_tasks(only_done=False)

            if not undone_tasks:
                print("Нет невыполненных задач.")
            else:
                print("Невыполненные задачи:")
                for i, task in enumerate(undone_tasks, start=1):
                    print(i, task)

            input("\nНажмите любую кнопку для продолжения...")
        elif choice == "8":
            cat = input("\nВведите категорию: ").strip().lower()
            if cat[0] != "#":
                cat = '#' + cat

            cat.lower()

            cat_tasks = tracker._list_tasks(category=cat)
            
            if not cat_tasks:
                print(f"Нет задач с категорией {cat}")
            else:
                print(f"Задачи с категорией {cat}:")
                for i, task in enumerate(cat_tasks, start=1):
                    print(i, task)

            input("\nНажмите любую кнопку для продолжения...")
        elif choice == "0":
            break
        else:
            print("Данного пункта нет в меню.")

    tracker._save_to_file(FILENAME)