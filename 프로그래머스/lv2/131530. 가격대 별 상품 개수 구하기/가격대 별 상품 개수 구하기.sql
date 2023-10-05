-- 코드를 입력하세요
SELECT
    CONCAT(SUBSTR(PRICE/10000,1,1),'0000') AS PRICE_GROUP
    ,COUNT(*) AS PRODUCTS
FROM
    PRODUCT
GROUP BY
    SUBSTR(PRICE/10000,1,1)
ORDER BY
    SUBSTR(PRICE/10000,1,1)