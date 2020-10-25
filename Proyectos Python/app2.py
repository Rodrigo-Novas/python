from importlib.machinery import SourceFileLoader

foo = SourceFileLoader("module.name", "C:/Users/novasrodrigo/Desktop/Rocketbot/services/libs/pytesseract/pytesseract.py").load_module()



