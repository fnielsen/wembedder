
function entity_to_label(entity, language='en') {
    if (language in entity['labels']) {
	return entity['labels'][language].value;
    }

    // Fallback
    languages = ['en', 'da', 'de', 'es', 'fr', 'jp',
		 'nl', 'no', 'ru', 'sv', 'zh'];
    for (lang in languages) {
	if (lang in entity['labels']) {
	    return entity['labels'][lang].value;
	}
    }

    // Last resort
    return entity['id']
}

