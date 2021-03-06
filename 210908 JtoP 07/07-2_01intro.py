# 메타 문자 : 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자
# . ^ $ * + ? { } [ ] \ | ( )




# 문자 클래스 character class []
# [ ] 사이의 문자들과 매치
# [abc] : a, b, c 중 한 개의 문자와 매치
# 'a', 'before', 'dude'가 있다고 할 때,
# 'a'와 'before'는 [abc]와 매치하지만,
# 'dude'는 abc 중 어느 하나도 포함하고 있지 않으므로 매치되지 않는다.

# []안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위를 의미한다.
# [a-c] = [abc], [0-5] = [012345]
# [a-zA-z] : 알파벳 모두
# [0-9] : 숫자

# 자주 사용하는 문자 클래스
# ^ 메타 문자를 사용할 경우, 반대(not)이라는 의미를 갖는다.
# 대문자로 사용된 것은 소문자의 반대
# \d : 숫자와 매치, [0-9]와 동일
# \D : 숫자가 아닌 것과 매치, [^0-9]와 동일
# \s : whitespace 문자와 매치, [ \t\n\r\f\v]와 동일
# \S : whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일
# \w : 문자 + 숫자와 매치, [a-zA-Z0-9_]와 동일
# \W : 문자 + 숫자가 아닌 문자와 매치, [^a-zA-z0-9_]와 동일





# Dot(.)
# 줄바꿈 문자인 \n을 제외한 모든 문자와 매치된다.
# a.b : a + 모든 문자 + b
# 'aab', 'a0b', 'abc'가 있다고 할 때,
# 'aab'의 가운데 a가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치
# 'a0b'의 가운데 0가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치
# 'abc'는 'a' 문자와 'b' 문자 사이에 어떤 문자라도 있어야 매치되므로 정규식과 매치되지 않는다.

# a[.]b : a + Dot(.)문자 + b
# a[.]b는 'a.b' 문자열과 매치되지만, 'a0b' 문자열과는 매치되지 않는다.





# 반복 (*)
# *는 * 바로 앞에 있는 문자가 0부터 무한대로 반복될 수 있다는 의미이다.
# ca*t
# 'ct' : 'a'가 0번 반복되어 매치
# 'cat' : 'a'가 0번 이상 반복되어 매치 (1번 반복)
# 'caaat' : 'a'가 0번 이상 반복되어 매치 (3번 반복)





# 반복 (+)
# +는 최소 1번 이상 반복될 때 사용한다.
# ca+t : c + a(1번 이상 반복) + t
# 'ct' : 'a'가 0번 반복되어 매치되지 않음
# 'cat' : 'a'가 1번 이상 반복되어 매치 (1번 반복)
# 'caaat' : 'a'가 1번 이상 반복되어 매치 (3번 반복)





# 반복 ({m,n}, ?)
# {} 메타 문자를 사용하면 반복 횟수를 고정할 수 있다.
# {m,n} 정규식을 사용하면 반복 횟수가 m부터 n까지 매치할 수 있다.
# 만약 {3,}처럼 사용하면 반복 횟수가 3 이상인 경우이고, {,3}처럼 사용하면 반복 횟수가 3 이하를 의미한다.
# 생략된 m은 0과 동일하며, 생략된 n은 무한대의 의미를 갖는다.
# {1,}은 +와 동일하고, {0,}은 *와 동일하다.

# 1. {m}
# ca{2}t : c + a(반드시 2번 이상 반복) + t
# 'cat' : 'a'가 1번만 반복되어 매치되지 않음
# 'caat' : 'a'가 2번 반복되어 매치

# 2. {m,n}
# ca{2,5}t : c + a(2~5회 반복) + t
# 'cat' : 'a'가 1번만 반복되어 매치되지 않음
# 'caat' : 'a'가 2번 반복되어 매치
# 'caaaaat' : 'a'가 5번 반복되어 매치
# 'caaaaaat' : 'a'가 6번 반복되어 매치되지 않음

# 3. ?
# 반복은 아니지만 ? 메타문자는 {0,1}을 의미한다.
# ab?c : a + b(있어도 되고 없어도 된다) + c
# 'abc' : 'b'가 1번 사용되어 매치
# 'ac' : 'b'가 0번 사용되어 매치

# *, +, ? 메타 문자는 모두 {m,n}형태로 고쳐쓰는 것이 가능하지만, 가급적 간결한 *, +, ? 메타 문자를 사용하자.
