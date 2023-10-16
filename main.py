import pandas as pd

def sum_excel_data(file_path):
    try:
        df = pd.read_excel(file_path)
        numeric_data = df.select_dtypes(include='number')
        total_sum = numeric_data.sum().sum()
        return total_sum
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def main():
    file_path = 'your_excel_file.xlsx'  # Укажите путь к вашему Excel файлу

    total_sum = sum_excel_data(file_path)
    if total_sum is not None:
        print(f"Сумма всех числовых данных в Excel файле: {total_sum}")

if __name__ == "__main__":
    main()
