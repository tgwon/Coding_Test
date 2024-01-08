-- 코드를 입력하세요

WITH a AS (
    SELECT
        c.daily_fee
        ,c.car_type
        ,h.history_id
        ,DATEDIFF(end_date, start_date) + 1 AS period,
    CASE 
        WHEN DATEDIFF(end_date, start_date) + 1 >= 90 THEN '90일 이상'
        WHEN DATEDIFF(end_date, start_date) + 1 between 30 and 89 THEN '30일 이상'
        WHEN DATEDIFF(end_date, start_date) + 1 between 7 and 29 THEN '7일 이상'
        ELSE 'NONE'
    END AS duration_type
FROM
    car_rental_company_rental_history AS h
    JOIN
    car_rental_company_car AS c
    ON c.car_id = h.car_id
WHERE
    c.car_type = '트럭')   

SELECT
    a.history_id, 
    ROUND(a.daily_fee * a.period * (100 - IFNULL(p.discount_rate,0)) * 0.01) AS FEE
FROM
    a
    LEFT JOIN
    car_rental_company_discount_plan AS p
    ON p.duration_type = a.duration_type 
    AND p.car_type = a.car_type
ORDER BY
    FEE DESC
    ,a.history_id DESC