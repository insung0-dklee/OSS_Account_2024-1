"""
사용자의 프로필 (이름, 나이, 이메일)을 입력받고, 
이름을 검색하여 다른 사람의 프로필을 검색할 수 있는 기능입니다.
"""

import json

class Profile: #프로필 class
    def __init__(self, name, age, email): #변수 초기화
        self.name = name #이름
        self.age = age #나이
        self.email = email #이메일
    
    def update_profile(self, name=None, age=None, email=None): #프로필 작성
        if name:
            self.name = name #이름 설정
        if age:
            self.age = age #나이 설정
        if email:
            self.email = email #이메일 설정
    
    def display_profile(self): #프로필 출력
        print("Name:", self.name) #이름 출력
        print("Age:", self.age) #나이 출력
        print("Email:", self.email) #이메일 출력
    
    def save_to_file(self, filename): #파일에 프로필 정보 저장
        profile_data = {
            "name": self.name,
            "age": self.age,
            "email": self.email
        }
        with open(filename, "w") as file:
            json.dump(profile_data, file)
    
    @staticmethod
    def load_from_file(filename): #프로필 정보 읽기
        with open(filename, "r") as file:
            profile_data = json.load(file)
        return Profile(profile_data["name"], profile_data["age"], profile_data["email"])

def get_user_profile(): #새 프로필 작성 함수
    name = input("Enter your name: ") #이름 입력
    while True: #숫자가 아닌경우 다시 입력 받음
        age_input = input("Enter your age: ") #나이 입력
        if age_input.isdigit():
            age = int(age_input)
            break
        else:
            print("Invalid input. Please enter a valid age.")
    email = input("Enter your email: ") #이메일 입력
    return Profile(name, age, email) #입력한 데이터 반환

def main(): #main 함수
    profile_filename = "profiles.json"
    profiles = []
    
    # 파일에서 기존 프로필 불러오기
    try:
        with open(profile_filename, "r") as file:
            profile_data = json.load(file)
        for data in profile_data:
            profiles.append(Profile(data["name"], data["age"], data["email"]))
        print("Profiles loaded from file.")
    except FileNotFoundError:
        print("No existing profiles found.")
    
    while True:
        choice = input("새로운 프로필 입력 = 1 / 프로필 검색 (이름) = 2 : ")
        if choice == "1" :
            # 새로운 사용자 프로필 입력
            print("Please enter your profile information.")
            user_profile = get_user_profile()
            profiles.append(user_profile)
        elif choice == "2" :
            # 사용자 이름으로 프로필 검색 및 출력
            search_name = input("Enter the name to search profile: ")
            found_profiles = [profile for profile in profiles if profile.name.lower() == search_name.lower()]
            if found_profiles:
                print(f"=== Found Profile(s) for {search_name} ===")
                for idx, profile in enumerate(found_profiles, start=1):
                    print(f"Profile {idx}:")
                    profile.display_profile()
                    print()
            else:
                print(f"No profile found for {search_name}.")
        else:
            break
        # 모든 프로필을 파일에 저장
        with open(profile_filename, "w") as file:
            profile_data = [{"name": profile.name, "age": profile.age, "email": profile.email} for profile in profiles]
            json.dump(profile_data, file)
        print("Profiles saved to file.")

if __name__ == "__main__":
    main()
