text = "это суперклассный текст на русском языке"
textSet = set(text)
letterSet = {'а', 'о', 'и', 'у', 'е', 'э', 'ю', 'я', 'ё'}

letterNotUsed = letterSet.difference(textSet)
print("Not used letters:", letterNotUsed)