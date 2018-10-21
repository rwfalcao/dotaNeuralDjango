function pick(url){
    $.ajax({
        url: url,
        type: 'get',
        dataType: 'json',
        success: function (data){
            console.log('teamZero: '+data.teamZero);
            console.log('teamOne: '+data.teamOne);

            $('.teamZero').html(data.html_team_zero)
            $('.teamOne').html(data.html_team_one)
        }
      });
}