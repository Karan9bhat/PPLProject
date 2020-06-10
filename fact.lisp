(defun factorial (n)
  (if (= n 0)
      1
      (* n (factorial (- n 1))) ) )

(write(factorial 5))

(defun fact (n)
  (defun fact-iter (n result)
    (if (= n 1)
        result
      (fact-iter (1- n) (* result n))))
  (fact-iter n 1))

(print(fact 19))
		
