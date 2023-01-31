-- 2022년 1월의 카테고리 별 도서 판매량을 합산하고, 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 카테고리명을 기준으로 오름차순 정렬해주세요.
-- 코드를 입력하세요
SELECT b.category, sum(bs.sales) as total_sales
from book b join book_sales bs on b.book_id = bs.book_id
where year(bs.sales_date) = 2022 and month(bs.sales_date) = 1
group by category
order by category;