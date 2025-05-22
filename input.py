todo_list = []

def show_menu():
    print("\n===== TO-DO MENU =====")
    print("1. Xem danh sách")
    print("2. Thêm công việc")
    print("3. Xóa công việc")
    print("4. Thoát")

def view_tasks():
    if not todo_list:
        print("Danh sách trống.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Nhập công việc: ")
    todo_list.append(task)
    print("✅ Đã thêm.")

def remove_task():
    view_tasks()
    try:
        index = int(input("Nhập số thứ tự để xóa: ")) - 1
        removed = todo_list.pop(index)
        print(f"🗑️ Đã xóa: {removed}")
    except (IndexError, ValueError):
        print("❌ Số không hợp lệ.")

while True:
    show_menu()
    choice = input("Chọn (1-4): ")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Tạm biệt!")
        break
    else:
        print("❗ Chọn sai, thử lại.")
