
function entity_to_label(entity, language='en') {
    if (language in entity['labels']) {
	return entity['labels'][language].value;
    }

    // Fallback
    languages = ['en', 'bn', 'da', 'de', 'es', 'fr', 'jp',
		 'nl', 'no', 'ru', 'sv', 'zh'];
    for (lang in languages) {
	if (lang in entity['labels']) {
	    return entity['labels'][lang].value;
	}
    }

    // Last resort
    return entity['id']
}


function hash_to_language() {
    var hash = window.location.hash;
    var regex = /language=(da|bn|de|en|es|fr|jp|nl|no|ru|sv|zh)/g;
    var match = regex.exec(hash);
    if (match) {
	language = match[1];
    }
    else {
	language = 'en';
    }
    return language;
}
