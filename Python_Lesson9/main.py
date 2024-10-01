from abc import ABC, abstractmethod

# class Animal(ABC):
#     def sound(self):
#         print('self')

class Processable(ABC):
    @abstractmethod
    def process():
        pass

class CreditCard(Processable):
    def process(self, amount):
        print(f"Processing credit card payment of {amount}")

class Paypal(Processable):
    def process(self, amount):
        print(f"Processing PayPal payment of {amount}")

class Crypto(Processable):
    def process(self, amount):
        print(f"Processing cryptocurrency payment of {amount}")
        
class PaymentProcessor:
    processor: 'Processable'

    def __init__(self, processor):
        self.processor = processor
    
    def process(self, amount):
        self.processor.process(amount)

# payementProcessor = PaymentProcessor(Crypto())
# payementProcessor.process(2000)

class Filterable(ABC):
    @abstractmethod
    def filter(self):
        pass

class AgeFilter(Filterable):
    def filter(self, data, min_age, max_age):
        return [item for item in data if min_age <= item['age'] <= max_age]

class CityFilter(Filterable):
    def filter(self, data, city):
        return [item for item in data if item['city'] == city]

class DataFilter:
    ifilter: 'Filterable'

    def __init__(self, filter) -> None:
        self.ifilter = filter

    def filter(self, *args, **kwargs):
        return self.ifilter.filter(*args, **kwargs)
    
data = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'New York'}
]
dataFilter = DataFilter(CityFilter())
print(dataFilter.filter(data, city = 'New York'))

class StatusFilter(Filterable):
    def filter(self, tasks, status):
        return [task for task in tasks if task.status == status]

class PriorityFilter(Filterable):
    def filter(self, tasks, priority):
        return [task for task in tasks if task.priority == priority]

class Sortable(ABC):
    @abstractmethod
    def sort(self):
        pass

from typing import List

class PrioritySort(Sortable):
    def sort(self,tasks: List['Task']):
        return sorted(tasks, key=lambda x: x.priority)

class TitleSort(Sortable):
    def sort(self,tasks):
        return sorted(tasks, key=lambda x: x.title)

class Task:
    def __init__(self, title, priority, status):
        self.title = title
        self.priority = priority  # 1 - высокая, 2 - средняя, 3 - низкая
        self.status = status # "completed", "in progress", "pending"

class TaskManager:
    ifilter: 'Filterable'
    isort: 'Sortable'
    def __init__(self, filter, sort):
        self.ifilter = filter
        self.isort = sort
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def filter(self, *args, **kwargs):
        self.ifilter.filter(self.tasks,*args, **kwargs)

    def sort(self):
        self.isort.sort(self.tasks)

# task_manager = TaskManager(PriorityFilter(), TitleSort())
# task_manager.add_task(Task("Write report", 1, "in progress"))
# task_manager.add_task(Task("Grocery shopping", 3, "pending"))
# task_manager.add_task(Task("Email client", 2, "completed"))

# print(task_manager.filter("pending"))
# print(task_manager.sort())
