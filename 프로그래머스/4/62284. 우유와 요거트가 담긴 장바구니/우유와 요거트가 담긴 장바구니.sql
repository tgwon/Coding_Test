-- 코드를 입력하세요
SELECT
    CART_ID
FROM
    CART_PRODUCTS
WHERE
    NAME = 'Yogurt'
    AND
    CART_ID in 
    (SELECT
        DISTINCT CART_ID
    FROM
        CART_PRODUCTS
    WHERE
        NAME = 'Milk')
order by
    cart_id