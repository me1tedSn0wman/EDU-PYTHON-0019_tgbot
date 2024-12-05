anonymous_filter = lambda x: type(x) is str and x.lower.count('a')>23



print(anonymous_filter('aaaaaa aaaa'))