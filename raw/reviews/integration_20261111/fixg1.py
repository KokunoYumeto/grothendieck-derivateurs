import pathlib
p = pathlib.Path(__file__).parent / 'new_I-b_GALOIS.tex'
s = p.read_text(encoding='utf-8')
a = "Cisinski2006Prefaisceaux"
assert s.count(a) == 1
s = s.replace(a, "Cisinski2006")
a = r"(1) The same extension $E_c\to B$ shows that, with 2-complete or 1-complete equivalences substituted throughout, a total equivalence"
assert s.count(a) == 1, 1
s = s.replace(a, r"(1) The same extension $E_c\to B$ shows that, with 2-complete equivalences substituted throughout, a total equivalence")
a = "So the assertion of ms.~84 withdrawn in footnote~41 is not repaired by the substitution."
assert s.count(a) == 1, 2
s = s.replace(a, a + " The substitution of 1-complete equivalences fails as well, by a different example which is not reproduced here.")
p.write_text(s, encoding='utf-8', newline='\n')
