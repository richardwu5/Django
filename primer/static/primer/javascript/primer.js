$(".hottake").on("click", ".fa-angle-up", function() {
	$(this).parent().next().toggle();
	$(this).parent().html("<i class='fa fa-angle-down'></i>");
	$(this).remove();
});

$(".hottake").on("click", ".fa-angle-down", function() {
	$(this).parent().next().toggle();
	$(this).parent().html("<i class='fa fa-angle-up'></i>");
	$(this).remove();
});