(clear-all)

(define-model memorize-words

(sgp :esc t :lf .05)

(chunk-type memorize state)
(chunk-type word word)

(add-dm
 (start-goal ISA memorize state nil)
 (apple ISA word word "apple")
 (banana ISA word word "banana")
 (cat ISA word word "cat")
 (dog ISA word word "dog")
 (elephant ISA word word "elephant"))

(p start-memorizing
   =goal>
     ISA         memorize
     state       nil
   ?retrieval>
     state       free
  ==>
   =goal>
     state       memorizing
   +retrieval>
     ISA         word)

(p continue-memorizing
   =goal>
     ISA         memorize
     state       memorizing
   =retrieval>
     ISA         word
     word        =word
  ==>
   !output!     (I memorized the word =word)
   +retrieval>
     ISA         word
     - word       =word)

(p stop-memorizing
   =goal>
     ISA         memorize
     state       memorizing
   ?retrieval>
     buffer      empty
  ==>
   =goal>
     state       done
   !output!     (I finished memorizing the words. Starting recall.))

(p start-recall
   =goal>
     ISA         memorize
     state       done
  ==>
   =goal>
     state       recalling
   +retrieval>
     ISA         word)

(p recall-word
   =goal>
     ISA         memorize
     state       recalling
   =retrieval>
     ISA         word
     word        =word
  ==>
   !output!     (I recalled the word =word)
   +retrieval>
     ISA         word
     - word       =word)

(p stop-recall
   =goal>
     ISA         memorize
     state       recalling
   ?retrieval>
     buffer      empty
  ==>
   =goal>
     state       finished
   !output!     (I finished recalling the words))

(goal-focus start-goal)

)