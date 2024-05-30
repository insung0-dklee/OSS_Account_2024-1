# ����� ���α׷�
# 1���� �Һ�о߿� ����ݾ��� �����ϴ� ��� ����

class HouseholdAccountBook:
    def __init__(self):
        self.entries = []

    def add_entry(self, category, amount):
        self.entries.append({'category': category, 'amount': amount})

    def show_entries(self):
        if not self.entries:
            print("�Էµ� ������ �����ϴ�.")
        else:
            print("����� ����:")
            total = 0
            for entry in self.entries:
                print(f"�о�: {entry['category']}, �ݾ�: {entry['amount']}��")
                total += entry['amount']
            print(f"�� ����: {total}��")

def run_account_book():
    account_book = HouseholdAccountBook()
    categories = ["�ĺ�", "�����", "��Ȱ��", "�Ƿ��", "������", "��Ÿ"]

    while True:
        print("\n�Һ�о߸� �����ϼ���:")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")
        print("0. ����")

        try:
            choice = int(input("����: "))
            if choice == 0:
                break
            elif 1 <= choice <= len(categories):
                category = categories[choice - 1]
                amount = int(input(f"{category} �ݾ��� �Է��ϼ���: "))
                account_book.add_entry(category, amount)
            else:
                print("�߸��� �����Դϴ�. �ٽ� �����ϼ���.")
        except ValueError:
            print("��ȿ�� ���ڸ� �Է��ϼ���.")

    account_book.show_entries()

def main():
    b_is_exit = False

    while not b_is_exit:
        func = input("��� �Է� (? �Է½� ����) : ")

        if func == "1":
            run_account_book()
        elif func == "2":
            print("��� 2�� ���� �������� �ʾҽ��ϴ�.")
        elif func == "3":
            print("��� 3�� ���� �������� �ʾҽ��ϴ�.")
        elif func == "?":
            print("����: \n1. ����� �Է�\n2. ��� 2\n3. ��� 3\n0. ����")
        elif func == "0":
            b_is_exit = True
        else:
            print("�߸��� �Է��Դϴ�. �ٽ� �õ��ϼ���.")

if __name__ == "__main__":
    main()
