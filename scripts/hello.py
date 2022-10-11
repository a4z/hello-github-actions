import sys
import platform

print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)


print("------------")
print(platform.python_version_tuple())
print(type(platform.python_version_tuple()))

print("Argument List:", str(sys.argv))
