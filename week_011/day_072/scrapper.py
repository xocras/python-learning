import requests
import pandas as pd
from bs4 import BeautifulSoup


def main():
    endpoint = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
    response = requests.get(endpoint)
    soup = BeautifulSoup(response.text, "html.parser")

    total_pages = int(soup.find_all("div", {"class": "pagination__btn--inner"})[-2].get_text(strip=True))

    pages = range(1, total_pages + 1)

    records = []

    for page in pages:
        endpoint = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page}"

        response = requests.get(endpoint)

        soup = BeautifulSoup(response.text, "html.parser")

        rows = soup.select('table tbody tr')

        for row in rows:

            cells = row.select('td .data-table__value')

            record = {
                "Undergraduate Major": cells[1].getText(),
                "Starting Median Salary": float(cells[3].getText().strip("$").replace(",", "")),
                "Mid-Career Median Salary": float(cells[4].getText().strip("$").replace(",", "")),
            }

            records.append(record)

        print(f"Page {page}/{total_pages}")

    pd.DataFrame(records).to_csv("salaries_by_college_major_updated.csv", index=False)

    print("Done!")


if __name__ == '__main__':
    main()
