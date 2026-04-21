        -- Запрос на среднюю зарплату в IT отделе
        SELECT AVG(salary) AS avg_it_salary
        FROM employees
        WHERE department = 'IT';
        
