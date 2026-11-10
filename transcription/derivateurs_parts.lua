-- Sets one five-page transcription file (a complete LaTeX document) inside the master, LesDerivateurs_transcription.tex.
-- The file is read as it is: its preamble definitions are applied inside a group (\newcommand defines locally), so
-- that macros of the same name defined differently in different files never meet; \DeclareMathOperator, which works
-- only in a preamble, is set as a command with \operatorname. The body (between \begin{document} and \end{document}) is
-- set in that group. Package loading, \usetikzlibrary and \frenchsetup lines are left to the master's preamble.
local M = {}

local function readfile(path)
  local f = assert(io.open(path, "rb"), "cannot open " .. path)
  local s = f:read("*a")
  f:close()
  return (s:gsub("\r\n", "\n"))
end

local function lastfind(s, needle)
  local at, pos = nil, 1
  while true do
    local a = s:find(needle, pos, true)
    if not a then return at end
    at, pos = a, a + 1
  end
end

function M.part(path)
  local s = readfile(path)
  local a, b = s:find("\\begin{document}", 1, true)
  local e = lastfind(s, "\\end{document}")
  assert(a and e, path .. ": not a complete LaTeX document")
  local pre, body = s:sub(1, a - 1), s:sub(b + 1, e - 1)
  local out = { "\\begingroup\\derpartstart{" .. path .. "}" }
  if pre:find("leqno", 1, true) then out[#out + 1] = "\\derleqno" end
  if pre:find("AutoSpacePunctuation=false", 1, true) then out[#out + 1] = "\\NoAutoSpacing" end
  for line in (pre .. "\n"):gmatch("(.-)\n") do
    local t = line:match("^%s*(.-)%s*$")
    if not (t:match("^\\documentclass") or t:match("^\\usepackage") or t:match("^\\usetikzlibrary")
            or t:match("^\\frenchsetup")) then
      line = line:gsub("\\DeclareMathOperator(%*?)%s*{?(\\%a+)}?%s*{([^}]*)}",
        function(star, cs, name) return "\\DeclareRobustCommand{" .. cs .. "}{\\operatorname" .. star .. "{" .. name .. "}}" end)
      out[#out + 1] = line
    end
  end
  -- a file that numbers its footnotes in its own way (\thefootnote redefined) starts its count afresh, as on its own
  local ownfn = pre:find("\\thefootnote", 1, true)
  if ownfn then out[#out + 1] = "\\edef\\derfnsaved{\\the\\value{footnote}}\\setcounter{footnote}{0}" end
  for line in (body .. "\n"):gmatch("(.-)\n") do out[#out + 1] = line end
  if ownfn then out[#out + 1] = "\\setcounter{footnote}{\\derfnsaved}" end
  out[#out + 1] = "\\endgroup"
  tex.print(out)
end

return M
