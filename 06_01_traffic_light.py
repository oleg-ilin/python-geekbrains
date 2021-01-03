import time
class Traffic_light:
    __color = ["красный", "желтый", "зеленый"]
    def switch_lights(self):
        print("Светофор включен, для выключения укажите значение 's' в файле stop_file.txt и сохраните его")
        while True:
            print(Traffic_light.__color[0])
            time.sleep(7)
            print(Traffic_light.__color[1])
            time.sleep(2)
            print(Traffic_light.__color[2])
            time.sleep(7)
            with open('stop_file.txt', 'r') as file:
                content = file.read(1)
                if content == "s":
                    print("Выключение светофора по команде s")
                    break
lights = Traffic_light()
lights.switch_lights()

