function setLanguage(language) {
    let form = document.getElementById('setLanguageForm');
    let field = document.getElementById('language_field');

    field.value = language;
    form.submit();
}