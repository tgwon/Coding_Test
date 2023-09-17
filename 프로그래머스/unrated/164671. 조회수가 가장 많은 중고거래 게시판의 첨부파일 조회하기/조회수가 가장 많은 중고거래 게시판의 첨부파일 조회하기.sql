-- 코드를 입력하세요
SELECT
    CONCAT('/home/grep/src/', 
           B.BOARD_ID, 
           '/', 
           FILE_ID, 
           FILE_NAME, 
           FILE_EXT) AS FILE_PATH
FROM
    USED_GOODS_BOARD AS B,
    USED_GOODS_FILE AS F
WHERE
    B.BOARD_ID = F.BOARD_ID
    AND
    B.VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
    -- inner join과 같은 의미! left join보다 성능 측면에서 좋음
ORDER BY
    FILE_ID DESC;