function goToPage(select) {
    var selectedOption = select.options[select.selectedIndex].value;
    if (selectedOption) {
        window.location.href = selectedOption;
    }
}