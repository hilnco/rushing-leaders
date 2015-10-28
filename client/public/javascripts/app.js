angular.module('statsApp', [])

.controller('mainController', function($scope, $http) {

    $scope.top10Data = {};

    // Get top 10 leading rushers
    $http.get('/top10')
        .success(function(data) {
            $scope.top10Data = data;
            console.log(data);
        })
        .error(function(error) {
            console.log('Error: ' + error);
        });

});




