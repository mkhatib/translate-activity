 #!/usr/bin/env python
try:
	from sugar.activity import bundlebuilder
	bundlebuilder.start()
except ImportError:
	import os
	os.system("find ./ | sed 's,^./,TranslateActivity.activity/,g' > MANIFEST")
	os.system('rm TranslateActivity.xo')
	os.chdir('..')
	os.system('zip -r TranslateActivity.xo TranslateActivity.activity')
	os.system('mv TranslateActivity.xo ./TranslateActivity.activity')
	os.chdir('TranslateActivity.activity')
