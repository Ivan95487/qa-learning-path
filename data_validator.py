# Простой скрипт для валидации данных 

def validate_users(user_list):
    print(f"Starting validation for {len(user_list)} users...\n")
    errors = 0
    
    for user in user_list:
        name = user.get("name")
        age = user.get("age")
        
        # Проверка 1: Имя не должно быть пустым
        if not name or name.strip() == "":
            print(f"[ERROR] User ID {user['id']}: Name is missing!")
            errors += 1
            
        # Проверка 2: Возраст должен быть числом от 18 до 100
        if not isinstance(age, int) or age < 18 or age > 100:
            print(f"[ERROR] User ID {user['id']}: Invalid age ({age})")
            errors += 1
            
    print(f"\nValidation finished. Found {errors} errors.")

# Тестовые данные
users_to_check = [
    {"id": 1, "name": "Ivan", "age": 25},
    {"id": 2, "name": "", "age": 30},      # Баг: пустое имя
    {"id": 3, "name": "Alex", "age": 15},  # Баг: слишком молодой
    {"id": 4, "name": "Petr", "age": "20"} # Баг: возраст строкой, а не числом
]

if __name__ == "__main__":
    validate_users(users_to_check)
