from tasks import task_1, task_2, task_3, task_4, task_5
from core.io import show_menu


def main():
    while True:
        task = show_menu()

        match task:
            case 1:
                task_1.task_1()
            case 2:
                task_2.task_2()
            case 3:
                task_3.MathClass.task_3()
            case 4:
                task_4.task_4()
            case 5:
                task_5.task_5()
            case 6:
                return


if __name__ == "__main__":
    main()
