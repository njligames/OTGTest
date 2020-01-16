
function numberOfOnes(val)
{
    var count = 0;
    var _val = val;

    while(_val)
    {
        count += (_val & 1);
        _val >>= 1;
    }
    return count;
}

function numberOfOnes_Recursive(val)
{
    if(val)
    {
        var add = (val & 1);
        val >>= 1;
        return numberOfOnes_Recursive(val) + add;
    }
    return 0;

}

function test_numberOfOnes()
{
    var i;
    const errorMsg = 'the functions do not return the same value';
    ;
    for (number = 0; number < 255; number++) {
        console.assert(numberOfOnes_Recursive(number) === numberOfOnes(number), {number: number, errorMsg: errorMsg});
        console.log((number).toString(2), numberOfOnes_Recursive(number));
    }
}
test_numberOfOnes();
