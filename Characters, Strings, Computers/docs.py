""" The word internationalization is commonly shortened to I18N. """

""" A classic form of ASCII code uses eight bits for each sign. Eight bits mean 256 different characters. 
The first 128 are used for the standard Latin alphabet (both upper-case and lower-case characters). """

""" A code point is a number which makes a character. For example, 32 is a code point which makes a space 
in ASCII encoding. We can say that standard ASCII code consists of 128 code points. """

""" Can you set the higher half of the code points differently for different languages? Yes, you can.
Such a concept is called a code page.

A code page is a standard for using the upper 128 code points to store specific national characters. 
For example, there are different code pages for Western Europe and Eastern Europe, Cyrillic and Greek alphabets,
Arabic and Hebrew languages, and so on."""

""" In consequence, to determine the meaning of a specific code point, you have to know the target code page.

In other words, the code points derived from the code page concept are ambiguous."""

# ---------------------------------------------------------------------------------------------------------------------

""" Unicode assigns unique (unambiguous) characters (letters, hyphens, ideograms, etc.) to more than a 
million code points. The first 128 Unicode code points are identical to ASCII, and the first 256 Unicode
code points are identical to the ISO/IEC 8859-1 code page (a code page designed for western European languages)."""

""" There is more than one standard describing the techniques used to implement Unicode in actual computers 
and computer storage systems. The most general of them is UCS-4.

The name comes from Universal Character Set.

UCS-4 uses 32 bits (four bytes) to store each character, and the code is just the Unicode code points' unique number.
A file containing UCS-4 encoded text may start with a [!]BOM (byte order mark), an unprintable combination of bits
announcing the nature of the file's contents. Some utilities may require it."""

# all Latin characters (and all standard ASCII characters) occupy eight bits;
# non-Latin characters occupy 16 bits;
# CJK (China-Japan-Korea) ideographs occupy 24 bits.

