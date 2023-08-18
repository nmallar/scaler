const delDuplicate = (arr) => { 
	
    let newArr = [];
      for (let i = 0; i < arr.length; i++) {
          let duplicateFound = false;
          
          for (let j = i + 1; j < arr.length; j++) {
              console.log(` i=${i} j=${j} arr[${i}]= ${arr[i]} arr[${j}]= ${arr[j]} - duplicateFound = ${duplicateFound} `)
              if (arr[i] === arr[j]) {
                  duplicateFound = true;
                  console.log(`duplicateFound = ${duplicateFound}`)
                  
              break;
              }
          }
          
          
          if (!duplicateFound) {
          newArr.push(arr[i]);
        }
        console.log(`newarr = ${newArr}`)
      }
    
      return newArr;
    };
    const arr = [1, 1, 2, 8, 5, 8]
    console.log(arr);
    const uniqueArr = delDuplicate(arr);    
    console.log(uniqueArr);