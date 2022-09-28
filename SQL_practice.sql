WITH correct_closed_accounts_cte AS 
(
   SELECT COUNT(*) AS numerator FROM account_status a 
   JOIN account_status b ON a.account_id = b.account_id 
   WHERE a.date = '2020-01-01' AND b.date = '2019-12-31' AND a.status = 'closed' AND b.status ='open'
),
num_accounts AS 
(
   SELECT numerator , COUNT(DISTINCT account_id) AS denominator 
   FROM correct_closed_accounts_cte , account_status WHERE date = 
   '2019-12-31' AND status ='open'
) 
SELECT CAST((numerator/denominator) AS DECIMAL(3,2)) AS percentage_closed FROM num_accounts; 


# Problem 2 
SELECT 
    p.title, 
    budget/num_employees AS budget_per_employee
FROM projects AS p
INNER JOIN (
    SELECT project_id, COUNT(*) AS num_employees
    FROM employee_projects
    GROUP BY 1
) AS ep
    ON p.id = ep.project_id
ORDER BY 2 DESC
LIMIT 5;

# Problem 3 
# Inner query gives, how many logins each user had between the two dates  
SELECT number_of_logins, count(*) AS number_of_users FROM
(
 SELECT user_id, COUNT(*) AS number_of_logins FROM user_logins
 WHERE login_date>='2022-01-01 00:00:00' AND login_date <'2022-01-02 00:00:00'
 GROUP BY user_id
) x
GROUP BY number_of_logins 


# PROBLEM 4
SELECT 
 u.name
 ,u.id AS user_id
 ,ROUND(SUM(p.price * t.quantity ) ,2) AS total_cost 
FROM users u 
INNER JOIN transactions t 
    ON u.id = t.user_id 
INNER JOIN products p 
    ON p.id = t.product_id 
GROUP BY u.name 
ORDER BY total_cost DESC

# Problem 5 
SELECT users.id, COUNT(comments.user_id) AS comment_count
FROM users
LEFT JOIN comments
    ON users.id = comments.user_id
        AND comments.created_at 
        BETWEEN '2020-01-01' AND '2020-01-31'
GROUP BY 1

# Problem 6  Filtering the null records 
SELECT n.name 
FROM neighborhoods n
LEFT JOIN users u
ON u.neighborhood_id = n.id 
WHERE u.id IS NULL 