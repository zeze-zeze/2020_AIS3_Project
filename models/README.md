## Classifiers

* sklearn.calibration.CalibratedClassifierCV
* sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis
* sklearn.ensemble.AdaBoostClassifier
* sklearn.ensemble.BaggingClassifier
* sklearn.ensemble.ExtraTreesClassifier
* sklearn.ensemble.GradientBoostingClassifier
* sklearn.ensemble.HistGradientBoostingClassifier
* sklearn.ensemble.RandomForestClassifier
* sklearn.ensemble.StackingClassifier # Complicated, Skipped
* sklearn.ensemble.VotingClassifier # Complicated, Skipped
* sklearn.gaussian_process.GaussianProcessClassifier
* sklearn.linear_model.PassiveAggressiveClassifier
* sklearn.linear_model.RidgeClassifier
* sklearn.linear_model.RidgeClassifierCV
* sklearn.linear_model.SGDClassifier
* sklearn.naive_bayes.GaussianNB
* sklearn.neighbors.KNeighborsClassifier  # Won't Perform well when training data is sparse
* sklearn.neighbors.RadiusNeighborsClassifier  # Won't Perform well when training data is sparse
* sklearn.neural_network.MLPClassifier
* sklearn.svm.SVC
* sklearn.tree.DecisionTreeClassifier
* sklearn.tree.ExtraTreeClassifier # Extra-trees should only be used within ensemble methods

## Regressors

* sklearn.compose.TransformedTargetRegressor
* sklearn.cross_decomposition.PLSRegression
* sklearn.ensemble.AdaBoostRegressor # Classifier Available
* sklearn.ensemble.BaggingRegressor # Classifier Available
* sklearn.ensemble.ExtraTreesRegressor # Classifier Available
* sklearn.ensemble.GradientBoostingRegressor # Classifier Available
* sklearn.ensemble.HistGradientBoostingRegressor # Classifier Available
* sklearn.ensemble.RandomForestRegressor # Classifier Available
* sklearn.ensemble.StackingRegressor # Complicated, Skipped
* sklearn.ensemble.VotingRegressor # Complicated, Skipped
* sklearn.gaussian_process.GaussianProcessRegressor # Classifier Available
* sklearn.isotonic.IsotonicRegression # Strictly Increasing Function only
* sklearn.kernel_ridge.KernelRidge
* sklearn.linear_model.ARDRegression
* sklearn.linear_model.BayesianRidge
* sklearn.linear_model.GammaRegressor # Predict values does not obey gamma distribution
* sklearn.linear_model.HuberRegressor
* sklearn.linear_model.LinearRegression
* sklearn.linear_model.LogisticRegression
* sklearn.linear_model.PassiveAggressiveRegressor # Classifier Available
* sklearn.linear_model.PoissonRegressor
* sklearn.linear_model.RANSACRegressor # Complicated, Skipped
* sklearn.linear_model.Ridge # Classifier Available
* sklearn.linear_model.SGDRegressor # Classifier Available
* sklearn.linear_model.TheilSenRegressor
* sklearn.linear_model.TweedieRegressor
* sklearn.neighbors.KNeighborsRegressor # Won't Perform well when training data is sparse
* sklearn.neighbors.RadiusNeighborsRegressor # Won't Perform well when training data is sparse
* sklearn.neural_network.MLPRegressor # Classifier Available
* sklearn.tree.DecisionTreeRegressor # Classifier Available
* sklearn.tree.ExtraTreeRegressor # Classifier Available