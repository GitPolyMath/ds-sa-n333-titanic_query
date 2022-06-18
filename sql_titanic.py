## 타이타닉 대시보드 만들기 위한 쿼리문 만들기 ##

# 1. 타이타닉 생존자 수 구하기

# select survived, count(*)
# from titanic
# group by survived;

# 2. 성별 타이타닉 생존자 수 구하기

# select survived, sex, count(*)
# from titanic
# group by survived, sex;

# 3. 성별 타이나틱 생존자 비율 구하기

# with
# temp as(
#     select  sex, count(*) as cnt_1
#     from titanic
#     group by sex
# ),
# temp_02 as(
#     select sex, survived, count(*) cnt_2
#     from titanic
#     group by sex, survived
# )

# select b.survived, b.sex, ((cnt_2+0.000)/cnt_1) as percentile
# from temp as a
#     join temp_02 as b on a.sex = b.sex
# group by b.sex, b.survived

# 4. Pclass별 생존자 비율 구하기

# with
# temp_01 as(
#     select pclass, survived, sum(survived) as sum_01
#     from titanic
#     group by pclass,survived
#     having survived = 1
# ),
# temp_02 as(
#     select pclass, count(*) as cnt_02
#     from titanic
#     group by pclass
# )

# select a.pclass, (b.sum_01+0.000)/a.cnt_02 as survived
# from temp_02 as a
#     join temp_01 as b on a.pclass = b.pclass;


# 5. Pclass 등급별, 성별 생존자 비율 구하기

# with
# temp_01 as(
#     select pclass, survived, sex, sum(survived) as sum_01
#     from titanic
#     group by pclass, survived, sex
# ),
# temp_02 as(
#     select pclass, sex, count(*) as cnt_02
#     from titanic
#     group by pclass, sex
# )

# select a.pclass, a.sex, (a.sum_01+0.00) / b.cnt_02 as percentile
# from temp_01 as a
#     join temp_02 as b on a.pclass = b.pclass
# group by a.pclass, a.survived, a.sex
# having survived = 1

# 6. 탑승위치별, Pclass, 성별, 생존자 비율 구하기

# -- 탑승위치별(embarked), Pclass별(pclass), 성별(sex), 생존자 비율 구하기

# with
# temp_01 as(
#     select pclass, embarked, sex, sum(survived) as sum_01
#     from titanic
#     group by pclass, embarked, sex
#     having embarked is not null
# ),
# temp_02 as(
#     select pclass, embarked, sex, count(*) as cnt_01
#     from titanic
#     group by pclass, embarked, sex
#     having embarked is not null
# )

# select a.pclass, a.embarked, a.sex, ((a.sum_01*1.00) / b.cnt_01) as percentile
# from temp_01 as a
#     join temp_02 as b on a.pclass = b.pclass and a.embarked = b.embarked and a.sex = b.sex