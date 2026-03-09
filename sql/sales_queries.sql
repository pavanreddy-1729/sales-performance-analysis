-- Total revenue
SELECT SUM(Quantity * Price) AS Total_Revenue
FROM sales_data;

-- Revenue by region
SELECT Region,
SUM(Quantity * Price) AS Revenue
FROM sales_data
GROUP BY Region;

-- Top selling product
SELECT Product,
SUM(Quantity) AS Total_Sales
FROM sales_data
GROUP BY Product
ORDER BY Total_Sales DESC;

-- Sales by category
SELECT Category,
SUM(Quantity * Price) AS Revenue
FROM sales_data
GROUP BY Category;
