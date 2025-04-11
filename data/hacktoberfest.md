kshyat idea on hacktoberfest initial commits for julia

example:
https://github.com/JuliaLang/julia/commit/c1d21e11a276ebf71b677076a064b5144c2e8f46

find docstring improvements
julia> Libc.strftime("%Y-%m-%d %H:%M:%S %Z", time())
"2022-10-18 09:20:15 CEST"

julia> Libc.strptime("%Y-%m-%d %H:%M:%S %Z", "2022-10-18 09:20:15 CEST")
Base.Libc.TmStruct(15, 20, 9, 18, 9, 122, 2, 290, 0, 0, 0, 0, 0, 0)



------------ivy

numpy methods:
implement tasks here: https://github.com/unifyai/ivy/issues/3607

argmax example:
https://github.com/unifyai/ivy/pull/4933/files