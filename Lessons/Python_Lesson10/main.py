from abc import ABC, abstractmethod
from typing import List

class IFilter(ABC):
    @abstractmethod
    def getFilters():
        pass
    @abstractmethod
    def getFileName():
        pass
    @abstractmethod
    def show():
        pass

class Photo(IFilter):
    def __init__(self, filename: str):
        self.filename = filename

    def getFilters(self):
        return 'Basic'
    
    def getFileName(self):
        return self.filename
    
    def show(self):
        print(f"Applying filters: {self.getFilters()} to {self.getFileName()}")

class SaturationFilter(IFilter):
    def __init__(self, obj: IFilter):
        self.obj = obj

    def getFilters(self):
        return f'Saturation, {self.obj.getFilters()}'
    
    def getFileName(self):
        return self.obj.getFileName()

    def show(self):
        print(f"Applying filters: {self.getFilters()} to {self.getFileName()}")

class BrightnessFilter(IFilter):
    def __init__(self, obj: IFilter):
        self.obj = obj

    def getFilters(self):
        return f'Brightness, {self.obj.getFilters()}'
    
    def getFileName(self):
        return self.obj.getFileName()

    def show(self):
        print(f"Applying filters: {self.getFilters()} to {self.getFileName()}")

class ContrastFilter(IFilter):
    def __init__(self, obj: IFilter):
        self.obj = obj

    def getFilters(self):
        return f'Contrast, {self.obj.getFilters()}'
    
    def getFileName(self):
        return self.obj.getFileName()

    def show(self):
        print(f"Applying filters: {self.getFilters()} to {self.getFileName()}")

# photo = Photo('Photos\\photo1.png')
# filtered1 = BrightnessFilter(photo)
# filtered2 = SaturationFilter(filtered1)
# filtered3 = ContrastFilter(filtered2)

# print(filtered2.getFilters())
# filtered3.show()


class Notification:
    def __init__(self, message: str):
        self.message = message
        self.sent_email = False
        self.sent_sms = False
    
    def send_email(self):
        self.sent_email = True
    
    def send_sms(self):
        self.sent_sms = True
    
    def send(self):
        channels = []
        if self.sent_email:
            channels.append("Email")
        if self.sent_sms:
            channels.append("SMS")
        return f"Message '{self.message}' sent via: {', '.join(channels)}"
    
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass
    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class WeatherData(Subject):
    def __init__(self):
        self.observers: List['Observer'] = []
    def register_observer(self, observer: Observer):
        self.observers.append(observer)
    def remove_observer(self, observer):
        self.observers.remove(observer)
    def _notify_observers(self):
        for observer in self.observers:
            observer.update()
    def event(self):
        self.notify_observers()

class CurrentConditionDisplay(Observer):
    def __init__(self, subject: Subject):
        self.weather_data = subject
        self.weather_data.register_observer(self)
    
    def update(self):
        print("I was Notified")

# weather_data = WeatherData()

# current_display = CurrentConditionDisplay(weather_data)
# weather_data.event()

class CaffeeineBeverage(ABC):

    def preepare_recepie(self):
        self.boilWater()
        self.prepare()
        self.pourInCup()
        self.addExtraCompnents()

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def addExtraComponents(self):
        pass

    def boil_water(self):
        print('Boiling water')

    def pourInCup(self):
        print("Pouring in a cup")

class Tea(CaffeeineBeverage):
    def prepare(self):
        print("preparing tea")

    def addExtraComponents(self):
        print("adding lemon")

# tea = Tea()
# tea.preepare_recepie()

