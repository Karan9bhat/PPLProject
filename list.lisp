(defun findnth (n list)
	(setq c 0)
	(dolist (l list)
		(incf c 1)
		(if (= c n)
			(return l)
		)
	)
)

(write(findnth 3 '(1 3 5 4 2 1)))