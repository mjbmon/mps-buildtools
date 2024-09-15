/*! \file tmisc/tmisc.h
    \brief Main header file for tmisc library.

    Details.
*/

#ifndef TMISC_H
#define TMISC_H 1

#define TMISC_MAJOR 1
#define TMISC_MINOR 1

/*!
 *  \addtogroup TLib
 *  @{
 */

//! Miscellaneous functions and classes.
namespace tmisc
{
const char *version();

/*!
 * A simple test class. The implementation
 * is in the file tmisc.cc
 * @brief Test class.
 * \headerfile tmisc/tmisc.h
 */
class tmps
{
 public:

    /*!
     * Create a new tmisc object.
     * @brief Default constructor.
     */
   tmps();
};

} // namespace tmisc

//! @} End of TLib group.

#endif // TMISC_H
