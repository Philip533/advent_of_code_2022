program aoc
    implicit none


    integer :: counter,i, size, istat,score

    character(len=1) :: a,b,trash,c,d

    open(unit=12,file="in.in",status="unknown")

    size = 0
    score = 0
    do
        read(12,*,iostat = istat) trash
        if(istat /= 0)exit
        size = size + 1
    end do
    rewind(12)
    do i = 1, size
        read(12,*)a,b
        if(a == "A" .and. b == "X")then
            score = score + 3
        else if(a == "A" .and. b == "Y")then
            score = score + 1
            score = score + 3
        else if(a == "A" .and. b == "Z")then
            score = score + 2
            score = score + 6
        else if(a == "B" .and. b == "X")then
            score = score + 1
        else if(a == "B" .and. b == "Y")then
            score = score + 2
            score = score + 3
        else if(a == "B" .and. b == "Z")then
            score = score + 3
            score = score + 6
        else if(a == "C" .and. b == "X")then
            score = score + 2
        else if(a == "C" .and. b == "Y")then
            score = score + 3
            score = score + 3
        else if(a == "C" .and. b == "Z")then
            score = score + 1
            score = score + 6
        end if
    end do
    print *, score

end program aoc
