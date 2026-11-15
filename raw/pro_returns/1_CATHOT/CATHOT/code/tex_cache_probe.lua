local lfs = require('lfs')
kpse.set_program_name('lualatex')
local cache = os.getenv('TEXMFCACHE')
print('env cache', cache)
print('kpse cache', kpse.expand_var('$TEXMFCACHE'))
for key, value in pairs(lfs.attributes(cache) or {}) do
  print('attribute', key, value)
end
print('isdir', lfs.isdir(cache))
print('isreadablefile', lfs.isreadablefile and lfs.isreadablefile(cache))
print('iswritablefile', lfs.iswritablefile and lfs.iswritablefile(cache))
local f, err = io.open(cache .. '/cathot_probe.tmp', 'wb')
print('io.open', f and 'success' or 'failure', err)
if f then f:close(); os.remove(cache .. '/cathot_probe.tmp') end
require('lualibs')
print('lualibs is_writable', file.is_writable(cache))
print('lualibs is_readable', file.is_readable(cache))
