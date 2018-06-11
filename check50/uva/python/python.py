import imp
import sys
import io
import contextlib
import check50

@contextlib.contextmanager
def _captureStdout(stdout=None):
	old = sys.stdout
	if stdout is None:
		stdout = io.StringIO()
	sys.stdout = stdout
	yield stdout
	sys.stdout = old

def load(filename):
	mod = imp.new_module(filename)
	with open(filename, "r") as f:
		src = f.read()
	exec(src, mod.__dict__) # TODO replace src with check50.open(filename).read()
	return PythonModule(mod)

class PythonModule:
	def __init__(self, module):
		self._module = module

	def has(self, attribute_name):
		if not hasattr(self._module, attribute_name):
			raise check50.Failure(f"{self._module.__name__} does not have {attribute_name}")
		return self

	def call(self, attribute_name, *args, **kwargs):
		with _captureStdout() as stdout:
			try:
				return_value = getattr(self._module, attribute_name)(*args, **kwargs)
			except BaseException as e:
				raise check50.Failure(f"{e} was raised during execution of {attribute_name}")
		return CallResult(return_value, stdout.getvalue())

class CallResult:
	def __init__(self, return_value, stdout):
		self.return_value = return_value
		self.stdout = stdout

class Mismatch(check50.Mismatch):
	pass
