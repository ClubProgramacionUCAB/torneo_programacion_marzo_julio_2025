
function singleNumber(nums) {

    let numDict = {};

    for (let i = 0; i < nums.length; i++) {
        if (numDict.hasOwnProperty(nums[i])) {
            numDict[nums[i]] += 1;
        }
        else {
            numDict[nums[i]] = 0;
        }
    }
    

    for (let i = 0; i < nums.length; i++) {
        if (numDict[nums[i]] === 0) {
            return nums[i];
        }
    }

    return 0;

}

