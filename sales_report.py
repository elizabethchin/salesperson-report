"""Generate sales report showing total melons each salesperson sold."""

def get_melons_sold_by_salesperson(log_file_path):
    mels_by_sales = {}

    with open(log_file_path) as f:
        for line in f:
            line = line.rstrip()

            salesperson_name, total_dollars, melons_sold = line.split('|') 

            if salesperson_name in mels_by_sales:
                mels_by_sales[salesperson_name] += int(melons_sold)
            else:
                mels_by_sales[salesperson_name] = int(melons_sold)
    return mels_by_sales

def print_sales_report(melons_sold_by_salesperson):
    for salesperson_name, melons_sold in melons_sold_by_salesperson.items():
        print(f"{salesperson_name} sold {melons_sold} melons")

print_sales_report(get_melons_sold_by_salesperson('sales-report.txt'))