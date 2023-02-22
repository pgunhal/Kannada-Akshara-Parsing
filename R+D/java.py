from jpype import *
startJVM(getDefaultJVMPath(), "-ea")
#parses the input into words (by space)
	private void parseWords() {
		String[] words = input.split(" ");
		int index = 0; //index of previous vowel

		for(String word: words) {
			index = 0;
			for(int i = 0; i < word.length(); i++) {
				if(isVowel(word.charAt(i))) {
					int v = i+1;
					if(i+2 == word.length()) {
						v = i+2;
					}
					aksharas.add(word.substring(index, v));
					index = i+1;
				}
			}
		}
	}
shutdownJVM()
