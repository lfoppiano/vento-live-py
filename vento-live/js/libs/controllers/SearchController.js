function SearchController($scope, $http) {

    $scope.excludeRetweets = true;
    $scope.nbNegatives = 0;
    $scope.nbPositives = 0;
    $scope.nbNeutros = 0;

    $scope.onKeyPress = function ($event) {
        if ($event.keyCode == 13) {
            $scope.newSearch();
        }
    }

    $scope.newSearch = function () {
        searchString = $scope.searchQuery + '+exclude:retweets+exclude:replies'

        //$http.get('http://vento-rest-test.elasticbeanstalk.com/classification/twitter/query/'+searchString +'/lang/en/')
        $http.get('http://localhost:8080/classification/twitter?query=' + searchString)
            //$http.get('http://localhost:8081/vento-live/berlusconi.json')
            .success(function (data) {
                $scope.tweets = data;

                data.forEach(function (element) {
                    if (element['score'] == '1') {
                        $scope.nbNegatives++;
                    } else if (element['score'] == '3') {
                        $scope.nbPositives++;
                    } else {
                        $scope.nbNeutros++;
                    }
                })
            });

    };
}
