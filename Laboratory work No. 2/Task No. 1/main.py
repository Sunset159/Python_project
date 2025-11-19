import json
import os
from typing import Any
from pathlib import Path

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

BASE_DIR = Path(__file__).parent 
FILENAME = BASE_DIR / "tasks.json" 

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
    
    def _status_done(self, index: int) -> None:
        self._get_task(index)._status_done()
    
    def _status_undone(self, index: int) -> None:
        self._get_task(index)._status_undone()

    def _list_tasks(self, only_done: bool | None = None, category: str | None = None) -> list[Task]:
        result = self._tasks

        if only_done is True:
            result = [temp for temp in result if temp.done]
        elif only_done is False:
            result = [temp for temp in result if not temp.done]

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
                "4 - Вывести все выполненные задачи\n" \
                "5 - Вывести все невыполненные задачи\n" \
                "6 - Вывести все задачи с заданной категорией\n" \
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
            cat = input("Введите категорию: ")
            
            if cat[0] != "#":
                cat = '#' + cat

            tracker._add_task(description, category=cat)

            print("Задача добавлена.")
            input("\nНажмите любую кнопку для продолжения...")            

        elif choice == "3":
            s
        elif choice == "4":
            s 
        elif choice == "5":
            s 
        elif choice == "6":
            s
        elif choice == "0":
            break

    print("\nОбновление задач...")
    tracker._save_to_file(FILENAME)