(* zad1 *)
(* a) *)

Goal forall X Y : Prop,
  ~(X /\ Y) \/ (~X /\ Y) \/ (~X /\ ~Y) <-> ~(X /\ Y).
Proof.
(* tauto. *)
intros. split.
- intros A B. destruct A.
  -- apply H. exact B.
  -- destruct H.
    --- apply H. destruct B. exact H0.
    --- apply H. destruct B. exact H1.
- intros A. left. exact A.
Qed.

(* b) *)
Goal forall X Y Z : Prop,
  ~(~X /\ Y /\ ~Z) /\ ~(X /\ Y /\ Z) /\ (X /\ ~Y /\ ~Z)
  <-> (X /\ ~Y /\ ~Z).
Proof.
intros. split.
- intros. destruct H. destruct H0. exact H1.
- now intros.
Qed.
