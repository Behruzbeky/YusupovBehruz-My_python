from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Status: {self.status}\n")


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print("✅ Task marked as complete.")
        else:
            print("❌ Invalid task number.")

    def list_all_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
        for i, task in enumerate(self.tasks, start=1):
            print(f"Task {i}:\n{task}")

    def display_incomplete_tasks(self):
        incomplete = [t for t in self.tasks if t.status == "Incomplete"]
        if not incomplete:
            print("🎉 All tasks are complete!")
        for i, task in enumerate(incomplete, start=1):
            print(f"Task {i}:\n{task}")


def main():
    todo_list = ToDoList()

    while True:
        print("\n📌 To-Do List Menu")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Display Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                datetime.strptime(due_date, "%Y-%m-%d")  # Validate date
                new_task = Task(title, description, due_date)
                todo_list.add_task(new_task)
                print("✅ Task added.")
            except ValueError:
                print("❌ Invalid date format.")

        elif choice == "2":
            todo_list.list_all_tasks()
            try:
                task_num = int(input("Enter task number to mark as complete: ")) - 1
                todo_list.mark_task_complete(task_num)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "3":
            todo_list.list_all_tasks()

        elif choice == "4":
            todo_list.display_incomplete_tasks()

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()







from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Date: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Content: {self.content}\n")


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("📭 No posts available.")
            return
        for i, post in enumerate(self.posts, start=1):
            print(f"Post {i}:\n{post}")

    def display_posts_by_author(self, author):
        filtered = [p for p in self.posts if p.author.lower() == author.lower()]
        if not filtered:
            print(f"❌ No posts found for author: {author}")
            return
        for i, post in enumerate(filtered, start=1):
            print(f"Post {i}:\n{post}")

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            removed = self.posts.pop(index)
            print(f"🗑️ Post '{removed.title}' deleted.")
        else:
            print("❌ Invalid post number.")

    def edit_post(self, index, new_title=None, new_content=None):
        if 0 <= index < len(self.posts):
            if new_title:
                self.posts[index].title = new_title
            if new_content:
                self.posts[index].content = new_content
            print("✏️ Post updated successfully.")
        else:
            print("❌ Invalid post number.")

    def latest_posts(self, count=3):
        if not self.posts:
            print("📭 No posts available.")
            return
        latest = sorted(self.posts, key=lambda p: p.created_at, reverse=True)[:count]
        for i, post in enumerate(latest, start=1):
            print(f"Latest Post {i}:\n{post}")


def main():
    blog = Blog()

    while True:
        print("\n📝 Blog Menu")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(Post(title, content, author))
            print("✅ Post added.")

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.display_posts_by_author(author)

        elif choice == "4":
            blog.list_all_posts()
            try:
                index = int(input("Enter post number to delete: ")) - 1
                blog.delete_post(index)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "5":
            blog.list_all_posts()
            try:
                index = int(input("Enter post number to edit: ")) - 1
                new_title = input("Enter new title (leave blank to keep current): ")
                new_content = input("Enter new content (leave blank to keep current): ")
                blog.edit_post(index, new_title or None, new_content or None)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "6":
            try:
                count = int(input("How many latest posts to show? "))
                blog.latest_posts(count)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "7":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()







class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ${amount:.2f} into account {self.account_number}.")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("⚠️ Insufficient funds. Overdraft not allowed.")
        else:
            self.balance -= amount
            print(f"✅ Withdrawn ${amount:.2f} from account {self.account_number}.")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.account_number in self.accounts:
            print("❌ Account already exists.")
        else:
            self.accounts[account.account_number] = account
            print(f"✅ Account {account.account_number} created successfully.")

    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f"💰 Balance for {account_number}: ${account.balance:.2f}")
        else:
            print("❌ Account not found.")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("❌ Account not found.")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("❌ Account not found.")

    def transfer(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if sender and receiver:
            if amount <= 0:
                print("❌ Transfer amount must be positive.")
            elif amount > sender.balance:
                print("⚠️ Insufficient funds for transfer.")
            else:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"✅ Transferred ${amount:.2f} from {from_acc} to {to_acc}.")
        else:
            print("❌ One or both accounts not found.")

    def display_account_details(self, account_number):
        account = self.find_account(account_number)
        if account:
            account.display_details()
        else:
            print("❌ Account not found.")


def main():
    bank = Bank()

    while True:
        print("\n🏦 Banking System Menu")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            try:
                balance = float(input("Enter initial balance: "))
                bank.add_account(Account(acc_num, name, balance))
            except ValueError:
                print("❌ Invalid balance amount.")

        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.check_balance(acc_num)

        elif choice == "3":
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter deposit amount: "))
                bank.deposit(acc_num, amount)
            except ValueError:
                print("❌ Invalid amount.")

        elif choice == "4":
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(acc_num, amount)
            except ValueError:
                print("❌ Invalid amount.")

        elif choice == "5":
            from_acc = input("Enter sender account number: ")
            to_acc = input("Enter receiver account number: ")
            try:
                amount = float(input("Enter transfer amount: "))
                bank.transfer(from_acc, to_acc, amount)
            except ValueError:
                print("❌ Invalid amount.")

        elif choice == "6":
            acc_num = input("Enter account number: ")
            bank.display_account_details(acc_num)

        elif choice == "7":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
